package com.example.repository

import com.example.model.apiDataItem
import io.ktor.client.*

class ApiInterfaceImplementation(
    client: HttpClient,
    private val apiInterface: ApiInterface
){
    private val clients = client
    suspend fun getList(): List<apiDataItem> {
        return apiInterface.getApiData(clients)
    }
}