package com.example

import com.example.model.apiDataItem
import io.ktor.client.*
import io.ktor.client.call.*

import io.ktor.client.engine.cio.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.request.*

import io.ktor.serialization.kotlinx.json.*
import kotlinx.serialization.json.Json

suspend fun main(args: Array<String>) {
    val client = HttpClient(CIO){
        install(ContentNegotiation) {
            json(Json {
                prettyPrint = true
                isLenient = true
            })
        }
    }
     val list:List<apiDataItem> = client.get("https://www.kontests.net/api/v1/all").body()
//         getapiData(client)
    list.forEach {
        println(it.name)
    }

}

suspend fun getapiData(client: HttpClient):List<apiDataItem> =   client.get("https://www.kontests.net/api/v1/all").body()

