$(document).ready(function(){
    getData();
    timeAlarm();
    ranking();
})

// 각각 데이터를 담아 둘 변수
var menu_list = [];
var datas = {};
var datas1 = {};
var colors = ['#0b62a4', '#DCE775', '#F48FBE', '#EC407E', '#7B1FA2', '#5E35BE','#BBDEFE', '#64B5FE', '#5C6BC0', '#303F9F', '#1565CE', '#82B1FE', '#80DEEE', '#00E5FE','#81C78E', '#00796B', '#5F6460'];
// 10초마다 갱신
setInterval(getData, 10000);
setInterval(timeAlarm, 1000);
function timeAlarm(){
    $("span#time").html(new Date(Date.now()));
}

// ajax로 데이터를 받아와 처리
function getData(){
    $.ajax({
        url : "{% url 'JY:getData' %}",
        type : "GET",
        data : {
            'csrfmiddlewaretoken': '{{ csrf_token }}',
        },
        success: function(res)
        {
            datas = res.datas;
            ranking();
            //ranking(res.rank);
            //$("#rank").html(res.rank + " ");
            Data_to(datas);
        }
    })
}
// 받아온 데이터 가공
function Data_to(a)
{
    menu_list = Object.keys(a.menu);
    datas1 = a.menu;
    datas1['y'] = "Twitter Datas Analysis by AJY";
    showGraph();
}


function ranking()
{ 
    $("#rank").empty();
    menu_list.forEach(function(menu, index) {
        var span = $("<span></span>");
        span.text(menu).prepend("<span>　</span>");
        span.find("span").css("background-color", colors[index]);
        $("#rank").append(span);
    });
}


// 가공한 데이터 그리기
function showGraph(){
    $("#datas").empty();
    Morris.Bar({
        element: 'datas',
        data: [
            datas1,
        ],
        barColors : colors,
        xkey: "y",
        ykeys: menu_list,
        labels: menu_list,
        hideHover : true
    });
}