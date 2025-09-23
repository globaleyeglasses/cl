app_name = "cocoleni_optics"
app_title = "COCO LENI Optics"
app_publisher = "COCO LENI"
app_description = "Optics Retail: Prescription, Lens Order, Face Scan 3D"
app_email = "hello@cocoleni.com"
app_license = "MIT"

fixtures = [
    {"dt": "Workspace", "filters": [["name", "=", "optics-retail"]]},
    {"dt": "Custom Field", "filters": [["name", "in", [
        "Sales Order-prescriptions",
        "Sales Order-lens_orders",
        "Sales Order Item-prescription",
        "Sales Order Item-lens_order"
    ]]]}
]
