package com.example.repository

import com.example.constants.ConstantVariables.BASE_URl
import com.example.model.apiDataItem
import io.ktor.client.*
import io.ktor.client.call.*
import io.ktor.client.request.*

interface ApiInterface {
    suspend fun getApiData(httpclient:HttpClient) :List<apiDataItem> = httpclient.get("$BASE_URl/v1/all").body()
}
