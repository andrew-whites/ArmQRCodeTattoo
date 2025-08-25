from flask import request
from flask.views import View


class DeleteContractByPIDView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == "GET":
            pids = list_pid()
            return render_template("contract/delete_patient_contract.html", pids=pids)
        else:
            pid = int(request.form['pid'])
            result = delete_patient_contract_pid(pid)
            if result == False:
                pids = list_pid()
                return render_template("contract/delete_patient_contract.html", pids=pids)
            contracts = selevt_all_patient_contract()
            return render_template("contract/list_patient_contract.html", contracts=contracts)
