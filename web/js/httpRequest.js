function postData(url,data,onload){
  var xhr = new XMLHttpRequest();
  xhr.open('POST', url);

  // set headers
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

  xhr.send(data);

  // listen for `load` even
  xhr.onload = () => {
    onload(xhr.responseText);
  }
}