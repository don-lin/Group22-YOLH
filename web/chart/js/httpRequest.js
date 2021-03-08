class Request {
  constructor() {}
  get(url, options) {
    return commonFetch(url, options, "GET");
  }
  post(url, options) {
    return commonFetch(url, options, "POST");
  }
  obj2String(obj, arr = [], idx = 0) {
    for (let item in obj) {
      arr[idx++] = [item, obj[item]];
    }
    return new URLSearchParams(arr).toString();
  }

  commonFetch(url, options, method = "GET") {
    const searchStr = obj2String(options);
    let initObj = {};
    if (method === "GET") {
      url += "?" + searchStr;
      initObj = {
        method: method,
        credentials: "include",
      };
    } else {
      initObj = {
        method: method,
        credentials: "include",
        headers: new Headers({
          Accept: "application/json",
          "Content-Type": "application/x-www-form-urlencoded",
        }),
        body: searchStr,
      };
    }

    fetch(url, initObj)
      .then((res) => {
        return res.json();
      })
      .then((res) => {
        return res;
      });
  }
}
