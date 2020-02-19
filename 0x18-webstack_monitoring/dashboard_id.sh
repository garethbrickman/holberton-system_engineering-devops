#!/usr/bin/env bash
# Requests Datadog API to get dashboard info, incl ID
api_key="18265caa751fea4117475be324d8d17a"
app_key="f172c0a1a45b805c87973931508b289b586f0a24"

curl -X GET \
-H "DD-API-KEY: ${api_key}" \
-H "DD-APPLICATION-KEY: ${app_key}" \
"https://api.datadoghq.com/api/v1/dashboard"
