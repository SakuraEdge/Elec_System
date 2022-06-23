
 function reload1(lst) {

     var myChart = echarts.init(document.getElementById('container'))

     console.log('我是饼图');

     var data = [], data2 = [];
     var trafficWay = [
         {
             name: '高价值型客户',
             value: lst[0]
         }, {
             name: '大众型客户',
             value: lst[1]
         }, {
             name: '潜力型客户',
             value: lst[2]
         }, {
             name: '低价值型客户',
             value: lst[3]
         }];
     var color = ['#2A8BFD', '#BAFF7F', '#00FAC1', '#FDE056', '#4ED33C', '#FF8A26', '#FF5252', '#9689FF', '#CB00FF']
     for (var i = 0; i < trafficWay.length; i++) {
         data.push({
             value: trafficWay[i].value,
             name: trafficWay[i].name,
             itemStyle: {
                 normal: {
                     borderWidth: 8,
                     shadowBlur: 20,
                     borderRadius: 20,
                     borderColor: color[i],
                     shadowColor: color[i]
                 }
             }
         }, {
             value: 5,
             name: '',
             itemStyle: {
                 normal: {
                     label: {
                         show: false
                     },
                     labelLine: {
                         show: false
                     },
                     color: 'rgba(0, 0, 0, 0)',
                     borderColor: 'rgba(0, 0, 0, 0)',
                     borderWidth: 0

                 }
             }
         });
         data2.push({
                 value: trafficWay[i].value,
                 name: trafficWay[i].name,
             },
             {
                 value: 5,
                 name: '',
                 itemStyle: {
                     normal: {
                         label: {
                             show: false
                         },
                         labelLine: {
                             show: false
                         },
                         color: 'rgba(0, 0, 0, 0)',
                         borderColor: 'rgba(0, 0, 0, 0)',
                         borderWidth: 0,
                         opacity: 0.2

                     }
                 }
             }
         )
     }

     let angle = 0;//角度，用来做简单的动画效果的
     option = {
         backgroundColor: "#181C41",
         color: color,
         legend: {
             right: '0%',
             top: '30%',
             icon: 'rect',
             itemWidth: 15,
             itemHeight: 15,
             textStyle: {
                 color: '#ffffff',
             }
         },
         series: [
             {//外线1

                 type: 'custom',
                 coordinateSystem: "none",
                 renderItem: function (params, api) {
                     return {
                         type: 'arc',
                         shape: {
                             cx: api.getWidth() / 2.7,
                             cy: api.getHeight() / 2,
                             r: Math.min(api.getWidth(), api.getHeight()) / 2 * 0.6,
                             startAngle: (0 + angle) * Math.PI / 180,
                             endAngle: (90 + angle) * Math.PI / 180
                         },
                         style: {
                             stroke: '#4EE9E6',
                             fill: "transparent",
                             lineWidth: 1.5
                         },
                         silent: true
                     };
                 },
                 data: [0]
             },
             {//内线1

                 type: 'custom',
                 coordinateSystem: "none",
                 renderItem: function (params, api) {
                     return {
                         type: 'arc',
                         shape: {
                             cx: api.getWidth() / 2.7,
                             cy: api.getHeight() / 2,
                             r: Math.min(api.getWidth(), api.getHeight()) / 2 * 0.6,
                             startAngle: (180 + angle) * Math.PI / 180,
                             endAngle: (270 + angle) * Math.PI / 180
                         },
                         style: {
                             stroke: "#4EE9E6",
                             fill: "transparent",
                             lineWidth: 1.5
                         },
                         silent: true
                     };
                 },
                 data: [0]
             },
             {//外线2

                 type: 'custom',
                 coordinateSystem: "none",
                 renderItem: function (params, api) {
                     return {
                         type: 'arc',
                         shape: {
                             cx: api.getWidth() / 2.7,
                             cy: api.getHeight() / 2,
                             r: Math.min(api.getWidth(), api.getHeight()) / 2 * 0.65,
                             startAngle: (270 + -angle) * Math.PI / 180,
                             endAngle: (40 + -angle) * Math.PI / 180
                         },
                         style: {
                             stroke: "#4EE9E6",
                             fill: "transparent",
                             lineWidth: 1.5
                         },
                         silent: true
                     };
                 },
                 data: [0]
             },
             {//外线2

                 type: 'custom',
                 coordinateSystem: "none",
                 renderItem: function (params, api) {
                     return {
                         type: 'arc',
                         shape: {
                             cx: api.getWidth() / 2.7,
                             cy: api.getHeight() / 2,
                             r: Math.min(api.getWidth(), api.getHeight()) / 2 * 0.65,
                             startAngle: (90 + -angle) * Math.PI / 180,
                             endAngle: (220 + -angle) * Math.PI / 180
                         },
                         style: {
                             stroke: "#4EE9E6",
                             fill: "transparent",
                             lineWidth: 1.5
                         },
                         silent: true
                     };
                 },
                 data: [0]
             },
             {//绿点1

                 type: 'custom',
                 coordinateSystem: "none",
                 renderItem: function (params, api) {
                     let x0 = api.getWidth() / 2.7;
                     let y0 = api.getHeight() / 2;
                     let r = Math.min(api.getWidth(), api.getHeight()) / 2 * 0.65;
                     let point = getCirlPoint(x0, y0, r, (90 + -angle))
                     return {
                         type: 'circle',
                         shape: {
                             cx: point.x,
                             cy: point.y,
                             r: 4
                         },
                         style: {
                             stroke: "#66FFFF",//粉
                             fill: "#66FFFF"
                         },
                         silent: true
                     };
                 },
                 data: [0]
             },
             {//绿点2
                 //绿点
                 type: 'custom',
                 coordinateSystem: "none",
                 renderItem: function (params, api) {
                     let x0 = api.getWidth() / 2.7;
                     let y0 = api.getHeight() / 2;
                     let r = Math.min(api.getWidth(), api.getHeight()) / 2 * 0.65;
                     let point = getCirlPoint(x0, y0, r, (270 + -angle))
                     return {
                         type: 'circle',
                         shape: {
                             cx: point.x,
                             cy: point.y,
                             r: 4
                         },
                         style: {
                             stroke: "#66FFFF",//粉
                             fill: "#66FFFF"
                         },
                         silent: true
                     };
                 },
                 data: [0]
             },
             {//绿点3

                 type: 'custom',
                 coordinateSystem: "none",
                 renderItem: function (params, api) {
                     let x0 = api.getWidth() / 2.7;
                     let y0 = api.getHeight() / 2;
                     let r = Math.min(api.getWidth(), api.getHeight()) / 2 * 0.6;
                     let point = getCirlPoint(x0, y0, r, (90 + angle))
                     return {
                         type: 'circle',
                         shape: {
                             cx: point.x,
                             cy: point.y,
                             r: 4
                         },
                         style: {
                             stroke: "#66FFFF",//粉
                             fill: "#66FFFF"
                         },
                         silent: true
                     };
                 },
                 data: [0]
             },
             {//绿点4
                 //绿点
                 type: 'custom',
                 coordinateSystem: "none",
                 renderItem: function (params, api) {
                     let x0 = api.getWidth() / 2.7;
                     let y0 = api.getHeight() / 2;
                     let r = Math.min(api.getWidth(), api.getHeight()) / 2 * 0.6;
                     let point = getCirlPoint(x0, y0, r, (270 + angle))
                     return {
                         type: 'circle',
                         shape: {
                             cx: point.x,
                             cy: point.y,
                             r: 4
                         },
                         style: {
                             stroke: "#66FFFF",//粉
                             fill: "#66FFFF"
                         },
                         silent: true
                     };
                 },
                 data: [0]
             },
             {
                 name: '',
                 type: 'pie',
                 clockWise: false,
                 radius: ['87%', '90%'],
                 hoverAnimation: false,
                 center: ['37%', '50%'],
                 top: "center",
                 itemStyle: {
                     normal: {
                         label: {
                             show: false
                         }
                     }
                 },
                 data: data
             },
             {
                 type: 'pie',
                 top: "center",
                 startAngle: 90,
                 clockwise: false,
                 center: ['37%', '50%'],
                 legendHoverLink: false,
                 hoverAnimation: false,
                 radius: ['85%', '50%'],
                 itemStyle: {
                     opacity: 0.15
                 },
                 label: {
                     show: false,
                     position: 'center'
                 },
                 labelLine: {
                     show: false
                 },
                 data: data2
             },
             {
                 name: '',
                 type: 'pie',
                 clockWise: false,
                 center: ['37%', '50%'],
                 radius: ['39%', '37%'],
                 hoverAnimation: false,
                 top: "center",
                 itemStyle: {
                     normal: {
                         label: {
                             show: false
                         }
                     }
                 },
                 data: data
             },
         ]
     };

     //获取圆上面某点的坐标(x0,y0表示坐标，r半径，angle角度)
     function getCirlPoint(x0, y0, r, angle) {
         let x1 = x0 + r * Math.cos(angle * Math.PI / 180)
         let y1 = y0 + r * Math.sin(angle * Math.PI / 180)
         return {
             x: x1,
             y: y1
         }
     }

     function draw() {
         angle = angle + 3
         myChart.setOption(option, true)
         //window.requestAnimationFrame(draw);
     }

     setInterval(function () {
         //用setInterval做动画感觉有问题
         draw()
     }, 150);

 }



 $(document).ready(function () {
   $("#show_avg_data").click(function () {
       $.get("/show/avg/data/", function (data) {
           data = data.trim().split(/\s+/)
           console.log(data[0])
           console.log(data[1])
           $("#show_avgMoney").html(data[0]);
           $("#show_avgTimes").html(data[1]);
       })
   });
});


$.get("/show/avg/data/", function (data) {
           data = data.trim().split(/\s+/)
           console.log(data[0])
           console.log(data[1])
           $("#show_avgMoney").html(data[0]);
           $("#show_avgTimes").html(data[1]);
       })


     $(document).ready(function () {
         $("#show_four_classes_data").click(function () {
             $.get("/show/four/classes/data/", function (data) {
                 data = data.trim().split(/\s+/)
                 $("#high_value_customers").html(data[0]);
                 $("#mass_customers").html(data[1]);
                 $("#potential_customers").html(data[2]);
                 $("#low_value_customers").html(data[3]);
                 lst = data;
                 console.log(data)
                 reload1(data);

             })
         });
     });


        $(document).ready(function () {
       $("#pre").click(function () {
           var money_pre = $('#money_pre').val();
           var times_pre = $('#times_pre').val();
            console.log(money_pre, times_pre);
           $.get("/show/pre/data/", {'money_pre': money_pre, 'times_pre': times_pre}, function (data) {
               $("#pre_result").html(data);
           })
       });
    });




  $(document).ready(function () {
       $("#pre_top5").click(function () {
           var now_date = $('#now_date').val();
           var month = $('#month').val();
            console.log(now_date, month);
           $.get("/show/pre/top5/", {'now_date': now_date, 'month': month}, function (lstData) {
               console.log(lstData)
               if(lstData === ''){
                   alert('您输入的数据为空或有误！')
                   $("#top5_error").html("数据输入为空或有误！");
               } else {
                   reload2(lstData['uid'], lstData['weight']);
               }
           })
       });
    });




function reload2(userList, weightList){
    console.log('我是闪烁的气泡图');

    var chart2 = echarts.init(document.getElementById("task4"));

    console.log(userList);
    console.log(weightList);

    var chartdata = [
        { name: userList[0], sum: weightList[0], size: 100 },
        { name: userList[1], sum: weightList[1], size: 90 },
        { name: userList[2], sum: weightList[2], size: 80 },
        { name: userList[3], sum: weightList[3], size: 70 },
        { name: userList[4], sum: weightList[4], size: 60 }
    ];
    var color = ['#6DFFA1', '#56C7F6', '#F9F08A','#6DFFA1', '#56C7F6', '#F9F08A'];
    var data=[]

    chartdata.map((item,index)=>{
        data.push(
            {
                name:'ID:' + item.name+'\n\n权重:'+item.sum,
                value: 111,
                symbolSize: item.size,
                draggable: true,
                label: {
                    normal: {
                        textStyle: {
                            fontSize: 12,
                            color: '#fff',
                        },
                    },
                },
                itemStyle: {
                    normal: {
                        color: new echarts.graphic.RadialGradient(0.5, 0.5, 1, [
                            {
                                offset: 0.2,
                                color: 'rgba(27, 54, 72, 0.2)',
                            },
                            {
                                offset: 0.8,
                                color: color[index],
                            },
                        ]),
                        opacity: 1,
                        borderWidth: 1,
                        borderColor: color[index],
                        shadowBlur: 7,
                        symbolOffset: 0.6,
                        shadowColor:color[index],
                    },
                },
            },
        )
    })

    let option1 = {
        backgroundColor: '#22284A',
        animationDurationUpdate: function (idx) {
            return idx * 100;
        },
        tooltip: {
            trigger: 'item',
            formatter: function (params, ticket, callback) {
                return params.data.tips || params.name;
            },
        },
        animationEasingUpdate: 'bounceIn',
        itemStyle: {
            // color: 'red',
        },
        cursor: 'pointer',
        series: [
            {
                type: 'graph',
                layout: 'force',
                cursor: 'pointer',
                force: {
                    repulsion: 200,
                    edgeLength: 100,
                },
                roam: true,
                label: {
                    normal: {
                        show: true,
                    },
                },

                data,
            },
        ],
    };

    chart2.setOption(option1);
}


$.get("/show/avg/data/", function (data) {
           data = data.trim().split(/\s+/)
           console.log(data[0])
           console.log(data[1])
           $("#show_avgMoney").html(data[0]);
           $("#show_avgTimes").html(data[1]);
       })

 $.get("/show/four/classes/data/", function (data) {
     data = data.trim().split(/\s+/)
     $("#high_value_customers").html(data[0]);
     $("#mass_customers").html(data[1]);
     $("#potential_customers").html(data[2]);
     $("#low_value_customers").html(data[3]);
     lst = data;
     console.log(data)
     reload1(data);
 })


$.get("/show/cla/echarts/data/", function (data) {
        console.log(data)
       three_type_cal(data['line_data'])
        classification_echarts(data['cla_flag'], data['cla_data'])
   })


$.get("/show/two/line/data/", function (data) {
    console.log(data)
})



localStorage.removeItem('obj');