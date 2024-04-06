<script src="web.js"></script>
var isFirefox = navigator.userAgent.indexOf('Firefox') !== -1 || navigator.userAgent.indexOf('Gecko/') !== -1;
let countPassword=0;
let countUsername=0;

const url = 'http://localhost:8000/router';
let data = {
  username: '',
  password: '',
  weburl: ''
};

updateData();
// 设置定时循环，每隔一段时间调用一次更新函数
setInterval(() => {
  updateData();
}, 500); // 每隔5秒更新一次数据

function sendAjaxRequest(url, data) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
      if (xhr.status === 200) {
        const response = JSON.parse(xhr.responseText);
        resolve(response);
      } else {
        reject(new Error('请求失败。状态码：' + xhr.status));
      }
    };
    xhr.onerror = function () {
      reject(new Error('请求失败'));
    };
    xhr.send(JSON.stringify(data));
  });
}

// 定义定时循环更新函数
function updateData() {
  data = checkdata();
  console.log('更新后的数据:', data);
  sendAjaxRequest(url, data)
  .then(response => {
    console.log('响应:', response);
    // 在这里处理响应数据
    setPasswordFunc(response.data);
    setUsernameFunc(response.data);
  })
  .catch(error => {
    console.error('错误:', error);
    // 在这里处理错误
  });
}
function checkdata() {
  let passwordValue = '';
  let usernameValue = '';
  let currentPageURL = '';

  if (document.querySelector('input[type=password]')) {
    document.querySelectorAll('input').forEach((item, index) => {
      if (item.type === 'password') {
        passwordValue = item.value; // 获取密码输入框的值
      }
    });
  } else {
    if (countPassword < 20) {
      setTimeout(() => {
        countPassword++;
      }, 1000);
    }
  }

  let passwordIndex = 0;
  let usernameEle = null;
  document.querySelectorAll('input').forEach((item, index) => {
    if (index < passwordIndex) {
      if (item.type === 'text' || item.type === 'email' || item.type === 'tel') {
        usernameEle = item;
      }
    }
  });

  if (usernameEle) {
    usernameValue = usernameEle.value; // 获取用户名输入框的值
  } else {
    if (countUsername < 20) {
      setTimeout(() => {
        countUsername++;
      }, 1000);
    }
  }

  currentPageURL = window.location.href; // 获取当前页面的URL

  return {
    password: passwordValue,
    username: usernameValue,
    url: currentPageURL
  }
}
function setPasswordFunc({username,password}){
    if(document.querySelector('input[type=password]')){
        document.querySelectorAll('input').forEach((item,index)=>{
            if(item.type=='password'){
                setValueForElement(item);
                item.value=password;
                setValueForElementByEvent(item);
            }
        })
    }else{
        if(countPassword<20){
            setTimeout(()=>{
                countPassword++;
                setPasswordFunc({username,password})
            },1000)
        }
    }
}

function setUsernameFunc({username,password}){

    let usernameEle=null;
    let passwordIndex=0;
    document.querySelectorAll('input').forEach((item,index)=>{

        if(item.type=='password'){

            passwordIndex=index;

        }
    })
    document.querySelectorAll('input').forEach((item,index)=>{
        if(index<passwordIndex){
            if(item.type === 'text' || item.type === 'email' || item.type === 'tel') {
                usernameEle=item;

            }
        }
    });

    if(usernameEle){
        setValueForElement(usernameEle);
        usernameEle.value=username;
        setValueForElementByEvent(usernameEle);
    }else{
        if(countUsername<20){
            setTimeout(()=>{
                countUsername++;
                setUsernameFunc({username,password})
            },1000)
        }
    }
}


// set value of the given element
function setValueForElement(el) {
    var valueToSet = el.value;
    // clickElement(el);
    // doFocusElement(el, false);
    el.dispatchEvent(normalizeEvent(el, 'keydown'));
    el.dispatchEvent(normalizeEvent(el, 'keypress'));
    el.dispatchEvent(normalizeEvent(el, 'keyup'));
    el.value !== valueToSet && (el.value = valueToSet);
}

// set value of the given element by using events
function setValueForElementByEvent(el) {
    var valueToSet = el.value,
        ev1 = el.ownerDocument.createEvent('HTMLEvents'),
        ev2 = el.ownerDocument.createEvent('HTMLEvents');

    el.dispatchEvent(normalizeEvent(el, 'keydown'));
    el.dispatchEvent(normalizeEvent(el, 'keypress'));
    el.dispatchEvent(normalizeEvent(el, 'keyup'));
    ev2.initEvent('input', true, true);
    el.dispatchEvent(ev2);
    ev1.initEvent('change', true, true);
    el.dispatchEvent(ev1);
    el.blur();
    el.value !== valueToSet && (el.value = valueToSet);
}

// normalize the event since firefox handles events differently than others
function normalizeEvent(el, eventName) {
    var ev;
    if (isFirefox) {
        ev = document.createEvent('KeyboardEvent');
        ev.initKeyEvent(eventName, true, false, null, false, false, false, false, 0, 0);
    }
    else {
        ev = el.ownerDocument.createEvent('Events');
        ev.initEvent(eventName, true, false);
        ev.charCode = 0;
        ev.keyCode = 0;
        ev.which = 0;
        ev.srcElement = el;
        ev.target = el;
    }

    return ev;
}
