$(document).ready(function () {
    $('#searchForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: "get-code/"+$('#search').val(),
            type: "get",
            success: function(e) {
                $("#s_result").empty();
                if (e.error) {
                    toastr.error(e.error);
                }else {
                    console.log(e);
                    $("#s_result").append('<div class="col-lg-6" style="margin-left: auto; margin-right: auto;"><div class="box_feat" id="icon_3"><h3>Prescription</h3><div class="row" style="padding-top: 30px;"><div class="col-lg-12 row" style="padding-bottom: 20px;"><div class="col-sm-5" style="text-align: left;"><strong>Date</strong></div><div class="col-sm-7" style="text-align: left;">'+e.data[0]+'</div></div><div class="col-lg-12 row" style="padding-bottom: 20px;"><div class="col-sm-5" style="text-align: left;"><strong>Patient Name</strong></div><div class="col-sm-7" style="text-align: left;">'+e.data[1]+'</div></div><div class="col-lg-12 row" style="padding-bottom: 20px;"><div class="col-sm-5" style="text-align: left;"><strong>Medicine</strong></div><div class="col-sm-7" style="text-align: left;">'+e.data[2]+'</div></div><div class="col-lg-12 row" style="padding-bottom: 20px;"><div class="col-sm-5" style="text-align: left;"><strong>Address</strong></div><div class="col-sm-7" style="text-align: left;">'+e.data[3]+'</div></div><div class="col-lg-12 row" style="padding-bottom: 20px;"><div class="col-sm-5" style="text-align: left;"><strong>Refills</strong></div><div class="col-sm-7" style="text-align: left;">'+e.data[4]+'</div></div><div class="col-lg-12 row" style="padding-bottom: 20px;"><div class="col-sm-5" style="text-align: left;"><strong>Amount</strong></div><div class="col-sm-7" style="text-align: left;">&#8358; '+e.data[5]+'</div></div><div class="col-lg-12 row" style="justify-content: center;padding-top: 20px;"><strong>Dr '+e.data[6]+'</strong></div></div></div></div>');
                    toastr.success(e.success);
                }
            }
        });
    });
});