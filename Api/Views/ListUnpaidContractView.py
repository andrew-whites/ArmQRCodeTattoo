from flask.views import View

class ListUnpaidContractView(View):
    def dispatch_request(self):
        contracts = select_all_unpaid_contracts()
        return render_template("contract/list_patient_contract.html", contracts=contracts)