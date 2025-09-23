app_name = "cocoleni_optics"
app_title = "COCO LENI Optics"
app_publisher = "COCO LENI"
app_description = "Optics Retail: Prescription, Lens Order, Face Scan 3D"
app_email = "hello@cocoleni.com"
app_license = "MIT"

# Always ship our Workspace + Custom Fields
fixtures = [
    {"dt": "Workspace", "filters": [["label", "=", "Optics Retail"]]},
    {"dt": "Custom Field", "filters": [
        ["dt", "in", ["Sales Order", "Sales Order Item"]],
        ["fieldname", "in", ["prescriptions", "lens_orders", "prescription", "lens_order"]]
    ]}
]
