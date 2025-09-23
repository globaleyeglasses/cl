# Add this to your cocoleni_optics/hooks.py
fixtures = [
    {"dt": "Workspace", "filters": [["name", "=", "optics-retail"]]},
    {"dt": "Custom Field", "filters": [["name", "in", [
        "Sales Order-prescriptions",
        "Sales Order-lens_orders",
        "Sales Order Item-prescription",
        "Sales Order Item-lens_order"
    ]]]}
]
