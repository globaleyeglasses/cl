# COCO LENI Optics (Frappe App)

Minimal ERPNext/Frappe app providing:
- Module: **Optics Retail**
- DocTypes: **Prescription**, **Lens Order**, **3D Face Scan**

## Install (self-hosted bench)
```bash
# unzip into bench/apps/
cd ~/frappe-bench/apps
unzip ~/Downloads/cocoleni_optics_full.zip

# make it a local git repo so `bench get-app` can register it
cd cocoleni_optics
git init
git add .
git commit -m "local app init"

# register app with bench (from bench root)
cd ~/frappe-bench
bench get-app cocoleni_optics apps/cocoleni_optics
bench --site yoursite.local install-app cocoleni_optics
bench --site yoursite.local migrate
bench clear-cache
```
