var listaEspaniol = {
  "sProcessing": "Procesando...",
  "sLengthMenu": "Mostrar _MENU_ registros",
  "sZeroRecords": "No se encontraron resultados",
  "sEmptyTable": "Ningún dato disponible en esta tabla =(",
  "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
  "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
  "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
  "sInfoPostFix": "",
  "sSearch": "Buscar:",
  "sUrl": "",
  "sInfoThousands": ",",
  "sLoadingRecords": "Cargando...",
  "oPaginate": {
    "sFirst": "<<",
    "sLast": ">>",
    "sNext": ">",
    "sPrevious": "<"
  },
  "oAria": {
    "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
    "sSortDescending": ": Activar para ordenar la columna de manera descendente"
  },
  "buttons": {
    "copy": "Copiar",
    "colvis": "Visibilidad"
  }
}

$(document).ready(function() {
  $('#dataTable').DataTable({
    columnDefs: [
      { width: "3%", targets: 0 }
    ],
    "language": listaEspaniol
  });
  $('#dtPacientes').DataTable({
    order: [[1, 'desc']],
    columns: [
        { width: "3%" },
        { orderable: false, width: "10%" },
        null,
        null,
        { orderable: false, width: "10%" },
        { orderable: false, width: "10%"  }
    ],
    "language": listaEspaniol
  });
});