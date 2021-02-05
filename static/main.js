
const tabledata = [];

$(document).ready(() => {
  loadTableData()
  initTable()
  initButtonEvents()
});

function loadTableData() {
  $.getJSON('api/data', (data) => {
    for (const x of data)
      tabledata.push(x);
  })
}

function initTable() {
  const table = new Tabulator('#example-table', {
    height: '311px',
    reactiveData: true,
    columns: [
      {title:'Active', field:'active', hozAlign:'center', editor:true, formatter:'tickCross'},
      {title:'Name', field:'name', width:150, editor:'input'},
      {title:'Email', field:'email', width:130, editor:'input'},
      {title:'Notes', field:'notes', width:130, editor:'input'},
      {title:'Progress', field:'progress', sorter:'number', hozAlign:'left', formatter:'progress', width:140, editor:true},
      {title:'Gender', field:'gender', editor:'select', editorParams:{values:{'male':'Male', 'female':'Female', 'unknown':'Unknown'}}},
      {title:'Rating', field:'rating',  formatter:'star', hozAlign:'center', width:100, editor:true},
    ],
    data: tabledata,
  });
}

function initButtonEvents() {
  $('#reactivity-add').on('click', () => {
      tabledata.push({name:'IM A NEW ROW', progress:100, gender:'male'});
  });

  $('#reactivity-delete').on('click', () => {
      tabledata.pop();
  });

  $.ajaxSetup({ contentType: 'application/json; charset=utf-8' });
  $('#reactivity-update').on('click', () => {
      const data = JSON.stringify(tabledata)
      $.post('api/data', data, (resp, status) => {
        console.log(resp, status)
      }, 'json')
  });
}