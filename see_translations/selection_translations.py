Translation = env['ir.translation']
field_name = object.name
model_name = object.model_id.model

labels_en = [tup[1] for tup in env[model_name].with_context(lang='en_US').fields_get([field_name])[field_name]['selection']]

name = "%s,%s" % (model_name, field_name)
domain = [('name', '=', name), ('type', '=', 'selection')]

for lang_code in env['res.lang'].search([('code', '!=', 'en_US')]).mapped('code'):
    for label in labels_en:
        if not Translation.search_count(domain + [('lang', '=', lang_code), ('src', '=', label)]):
            Translation.create({
                'module': '__custo__',
                'type': 'selection',
                'name': name,
                'lang': lang_code,
                'source': label
                })

action_dict = env['ir.actions.act_window'].for_xml_id('base', 'action_translation')
action_dict.update({
    'domain': domain
})
action = action_dict
