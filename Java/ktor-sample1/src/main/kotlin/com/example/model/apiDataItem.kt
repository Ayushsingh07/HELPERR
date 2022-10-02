package com.example.model


import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class apiDataItem(
    @SerialName("duration")
    val duration: String,
    @SerialName("end_time")
    val endTime: String,
    @SerialName("in_24_hours")
    val in24Hours: String,
    @SerialName("name")
    val name: String,
    @SerialName("site")
    val site: String,
    @SerialName("start_time")
    val startTime: String,
    @SerialName("status")
    val status: String,
    @SerialName("url")
    val url: String
)