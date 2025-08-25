from flask import request
from flask.views import MethodView


class ContracrView(MethodView):
    def get(self):
        return render_template("contract/add_patient_contract.html")
    
    def post(self):
        pid = request.form['pid']
        approver = request.form['approver']

        # .......

        result = insert_patient_contract(pid=int(pid), approved_by=approver, approved_date=approved_date, hcp=hcp, 
                                         payment_mode=payment_mode, amount_paid=float(amount_paid), amount_due=float(amount_due))
        
        if result == False:
            return render_template("contract/add_patient_contract.html")
        contracts = select_all_patient_contract()
        return render_template("contract/list_patient_contract.html", contracts=contracts)