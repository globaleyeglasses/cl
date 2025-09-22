frappe.ui.form.on('Prescription', {
  pd_od: function(frm){ refresh_total(frm); },
  pd_os: function(frm){ refresh_total(frm); },
  refresh: function(frm){ refresh_total(frm); }
});
function refresh_total(frm){
  const t = (frm.doc.pd_od || 0) + (frm.doc.pd_os || 0);
  frm.set_value('pd_total', t || null);
}
