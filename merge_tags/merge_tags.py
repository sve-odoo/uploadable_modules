tags = object.x_tag_ids
partners = tags.mapped('partner_ids')
env['res.partner.category'].create({
    'name': object.x_name,
    'partner_ids': [(6, 0, partners.ids)]
    })
tags.write({'active': False})
