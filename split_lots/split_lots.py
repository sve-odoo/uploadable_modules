Lot = env['stock.production.lot']
packop = env['stock.pack.operation'].browse(context['packop_id'])
new_qty = packop.product_qty
for line in object.x_line_ids:
    new_qty -= line.x_qty
    line_lot = Lot.create({
        'name': line.x_name,
        'product_id': packop.product_id.id
        })
    packop.copy({
        'product_qty': line.x_qty,
        'lot_id': line_lot.id
        })
if new_qty > 0:
    packop.write({'product_qty': new_qty})
else:
    packop.unlink()
action = {
    'type': 'ir.actions.client',
    'tag': 'reload',
}