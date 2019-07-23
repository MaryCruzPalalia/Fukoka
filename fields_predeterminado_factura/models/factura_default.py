# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models
# modelo de campos a editar desde factura borrados

class editable_invoice(models.Model):
	_inherit = 'account.invoice'


	@api.model
	def create(self, vals):
		factura=super(editable_invoice,self).create(vals)
		print("hola2")
		id_x= self.env['res.partner'].search([('id', '=', factura.partner_id.id)])
		print(id_x.Transferenciaelectronica_Uso)
		factura.write({'l10n_mx_edi_partner_bank_id': id_x.Banco_asociado.id,'l10n_mx_edi_payment_method_id':id_x.Metodo_pago.id,
	       	'l10n_mx_edi_usage':id_x.Transferenciaelectronica_Uso }) #se utiliza el valor del select para pasar el tipo que es y deben tener el mismo valor que el original
		return factura
