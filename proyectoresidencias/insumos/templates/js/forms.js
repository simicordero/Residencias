
function getData() {
    tbl = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'formFamilia',
                'id': id
            },
            dataSrc: ""
        },
        columns: [
            {"data": "nombre"}
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" class="btn btn-default"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" class="btn btn-default"><i class="fas fa-ban"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function () {
    getData();

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        $('form')[0].reset();
        $('#modalEmpresaIMSS').modal('show');
    })

    $('form').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Desea Guardar?', parameters, function () {
            $('#modalEmpresaIMSS').modal('hide');
            tbl.ajax.reload();
        });
    });
});