a = {
  "retcode": 0,
  "message": "OK",
  "data":
      {
    "iTotal": 23,
    "list": [
      {
        "sChanId": [
          "732",
          "727"
        ],
        "sTitle": "琴",
        "sIntro": ""
        # .....
      }]
  }
}
print(a['data']['list'][0]['sTitle'])