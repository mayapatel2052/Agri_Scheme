$(document).ready(function () {
    $('#myselection').on('change', function () {
        var demovalue = $(this).val();
        $("div.myDiv").hide();
        $("#" + demovalue).show();
    });
    $("#farmer").show();

    $("#add_sch").click(function () {
        $("#add_sch_form").show();
    });
    $("#cls_sch").click(function () {
        $("#add_sch_form").hide();
    });
    $("#add_sch_form").hide();
});

