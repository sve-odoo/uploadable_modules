name = "%s,%s" % (object.model_id.model, object.name)
domain = [('name', '=', name), ('type', '=', 'field')]
source = model.with_context(dict(context, lang=None)).browse(object.id).field_description

context.update({
    'default_module': '__custo__',
    'default_type': 'field',
    'default_name': name,
    'default_source': source
    })

action_dict = env['ir.actions.act_window'].for_xml_id('base', 'action_translation')
action_dict.update({
    'domain': domain,
    'context': context,
})
action = action_dict
