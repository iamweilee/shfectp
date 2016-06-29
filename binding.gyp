{
  "targets": [
    {
      "target_name": "shifctp",
      "sources": [ "src/shifctp.cc","src/tools.cc","src/stdafx.cpp","src/uv_mduser.cpp","src/uv_trader.cpp","src/wrap_mduser.cpp","src/wrap_trader.cpp" ],
      "libraries":["/root/github/node-ctp/v6.3.6_20151215_api_tradeapi_linux64/thostmduserapi.so","/root/github/node-ctp/v6.3.6_20151215_api_tradeapi_linux64/thosttraderapi.so"],
      "include_dirs":["v6.3.6_20151215_api_tradeapi_linux64/"]
    }
  ],
}


