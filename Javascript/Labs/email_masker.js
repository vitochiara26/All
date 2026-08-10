function maskEmail(email) {
    const maskedPart = email.slice(1, email.indexOf('@') - 1)
    email = email.replace(maskedPart, '*'.repeat(maskedPart.length))
    return email
}

const email = "apple.pie@example.com"
console.log(maskEmail(email))

const email2 = "freecodecamp@example.com"
console.log(maskEmail(email2))

const email3 = "info@test.dev"
console.log(maskEmail(email3))

const email4 = "user@domain.org"
console.log(maskEmail(email4))
