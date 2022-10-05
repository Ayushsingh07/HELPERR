function generate(n) {
    var add = 1, max = 12 - add;   // 12 is the min safe number Math.random() can generate without it starting to pad the end with zeros.   

    if (n > max) {
        return generate(max) + generate(n - max);
    }

    max = Math.pow(10, n + add);
    var min = max / 10; // Math.pow(10, n) basically
    var number = Math.floor(Math.random() * (max - min + 1)) + min;

    return ("" + number).substring(add);
}


//Function to send OTP

function sendOtp(mobile, otp) {
    const body = {
        "messaging_product": "whatsapp",
        "to": mobile,
        "type": "template",
        "template": {
            "name": "my_otp",
            "language": {
                "code": "en"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": otp
                        }
                    ]
                }
            ]
        }
    }
    //token is from mayanksingh.work@gmail.com, this is temp token
    const response = fetch('https://graph.facebook.com/v13.0/<mobileId>/messages', {
        method: 'post',
        body: JSON.stringify(body),
        headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer <TOKEN>' },
    })
    console.log(response)
    console.log(response)

    return response
}

let otp = generate(6)
const otpResponse = sendOtp(num, otp) //num will be the number of the reciver
