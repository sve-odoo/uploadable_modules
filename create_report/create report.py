xmlid_mod = pool['ir.model.data']
view_mod = pool['ir.ui.view']
report_mod = pool['ir.actions.report.xml']
module = "__custo__"

if object.x_type == 'internal':
    layout_tname = 'report.internal_layout'
elif object.x_type == 'external':
    layout_tname = 'report.external_layout'

# The report_name is going to be constructed as a concatenation of:
# - The name of the module ( by default __custo__ )
# - A dot
# - The word "report"
# - An underscore
# - The name of the model, removed from any non strictly alphanumeric character
# - An underscore
# - The user-friendly name of the report, removed from any non strictly alphanumeric character
# - An underscore
# - document
# Ex: __custo__.report_saleorder_orderconfirmation_document

accepted_chars = map(chr, range(ord('a'), ord('z')+1)) + map(chr, range(ord('0'), ord('9')+1))

name_short = ''.join(c for c in object.x_name.lower() if c in accepted_chars)
model_short = ''.join(c for c in object.x_model_id.model.lower() if c in accepted_chars)

technical_name = 'report_' + model_short + '_' + name_short

document_technical_name = technical_name + '_document'

document_tname = module + '.' + document_technical_name

document_qweb = """<?xml version="1.0"?>
<t t-name="%s">
    <t t-call="%s">
        <div class="page">

            <h2>Title of your report</h2>

            <div class="row mt32 mb32" id="information">
                <div class="col-xs-3">
                    <strong>Block1:</strong>
                    <p>Content1</p>
                </div>
                <div class="col-xs-3">
                    <strong>Block2:</strong>
                    <p>Content2</p>
                </div>
            </div>

            <table class="table table-condensed">
            <thead>
                <tr>
                    <th>Col1</th>
                    <th>Col2</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                        <span>Content1</span>
                    </td>
                    <td>
                        <span>Content2</span>
                    </td>
                </tr>
            </tbody>
            </table>

            <p>
                <strong>Additional note: </strong>
                <span>Note</span>
            </p>

        </div>
    </t>
</t>
""" % (document_tname, layout_tname)

# Create the "document" QWeb view,
document_view_values = {
    'name': document_technical_name,
    'model': 'ir.ui.view',
    'type': 'qweb',
    'arch': document_qweb,
}
document_view_id = view_mod.create(cr, uid, document_view_values, context=context)
# and an XMLID for it
document_xmlid_values = {
    'module': module,
    'name': document_technical_name,
    'model': 'ir.ui.view',
    'res_id': document_view_id,
}
xmlid_mod.create(cr, uid, document_xmlid_values, context=context)

if object.x_translate:
    translate_tname = module + '.' + technical_name
    translate_qweb = """<?xml version="1.0"?>
<t t-name="%s">
    <t t-call="report.html_container">
        <t t-foreach="doc_ids" t-as="doc_id">
            <t t-raw="translate_doc(doc_id, doc_model, '%s', '%s')"/>
        </t>
    </t>
</t>""" % (translate_tname, object.x_lang_path, document_tname)

    # Create the "caller" or "translator" QWeb view,
    translate_view_values = {
        'name': technical_name,
        'model': 'ir.ui.view',
        'type': 'qweb',
        'arch': translate_qweb,
    }
    translate_view_id = view_mod.create(cr, uid, translate_view_values, context=context)
    # and an XMLID for it
    translate_xmlid_values = {
        'module': module,
        'name': technical_name,
        'model': 'ir.ui.view',
        'res_id': translate_view_id,
    }
    xmlid_mod.create(cr, uid, translate_xmlid_values, context=context)

# Create the report
report_values = {
    'name': object.x_name,
    'model': object.x_model_id.model,
    'report_type': 'qweb-pdf',
    'report_name': translate_tname if object.x_translate else document_tname,
}
report_id = report_mod.create(cr, uid, report_values, context=context)
# And an action binding (shortcut to the report in the "Print" menu)
action_binding_values = {
    'name': object.x_name,
    'model': object.x_model_id.model,
    'key2': 'client_print_multi',
    'value': 'ir.actions.report.xml,%d' % (report_id),
}
pool['ir.values'].create(cr, uid, action_binding_values, context=context)

# We're done.
# Delete the "wizard" from the database
self.unlink(cr, uid, object.id, context=context)

# And display the newly created report
action_dict = pool['ir.actions.act_window'].for_xml_id(cr, uid, 'base', 'ir_action_report_xml', context=context)
action_dict.update({
    'res_id': report_id,
    'view_mode': 'form,tree'
    })
action_dict.pop('views')
action_dict.pop('view_id')
action = action_dict
