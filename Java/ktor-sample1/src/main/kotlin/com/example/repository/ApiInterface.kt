package com.example.repository

import io.ktor.client.*
import io.ktor.client.request.*

interface ApiInterface {
    suspend fun getApiData(httpclient:HttpClient)= httpclient.get("https://www.kontests.net/api/v1/all")
}
