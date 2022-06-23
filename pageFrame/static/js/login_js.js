$(document).ready(function () {
   $("#login").click(function () {
       //定义用户与密码
       var account = $('#account').val();
       var password = $('#password').val();
        console.log(money_pre, times_pre);
       $.get("/show/pre/data/", {'account': account, 'password': password}, function () {
           $("#pre_result").html(data);
       })
   });
});