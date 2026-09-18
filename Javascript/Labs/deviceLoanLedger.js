const equipmentLedger = {
    "1": { type: "PC", status: "CheckedOut", 
    borrower: { name: "John Smith", email: "john@acme.org" }, dueDate: "11/30/2025" },

    "2": { type: "Laptop", status: "CheckedIn", borrower: { name: "", email: "" }, dueDate: "" },
    
    "3": { type: "Laptop", status: "CheckedOut", 
    borrower: { name: "Jane Doe", email: "jane@acme.org" }, dueDate: "10/31/2025" },

    "4": { type: "iPad", status: "CheckedIn", borrower: { name: "", email: "" }, dueDate: "" }
};

function checkoutDevice(ledger, assetTag, borrower) {
    if (!ledger.hasOwnProperty(assetTag)) {
        return {
            ledger: ledger,
            message: `Device with asset tag "${assetTag}" was not found.`
        };
    }

    if (ledger[assetTag].status === "CheckedOut") {
        return {
            ledger: ledger,
            message: `Device "${assetTag}" is already 
            checked out to ${ledger[assetTag].borrower.name}.`
        };
    }

    const updatedLedger = JSON.parse(JSON.stringify(ledger));
    const device = updatedLedger[assetTag];

    device.status = "CheckedOut";
    device.borrower = {
        name: borrower.name,
        email: borrower.email
    };
    if (borrower.dueDate) {
        device.dueDate = borrower.duDate;
    }

    return {
        ledger: updatedLedger,
        message: `Device "${assetTag}" successfully checked out to ${borrower.name}.`
    };
}

function checkinDevice(ledger, assetTag) {
    if (!ledger.hasOwnProperty(assetTag)) {
        return {
            ledger: ledger,
            message: `Device with asset tag "${assetTag}" was not found.`
        };
    }

    const updatedLedger = JSON.parse(JSON.stringify(ledger));
    const device = updatedLedger[assetTag];

    device.status = "CheckedIn";
    device.borrower = {
        name: "",
        email: ""
    };
    device.dueDate = "";

    return {
        ledger: updatedLedger,
        message: `Device "${assetTag}" successfully checked in.`
    };
}

function parseDateValue(dateStr) {
    if (!dateStr) return 0;
    const [month, day, year] = dateStr.split("/").map(Number);
    return year * 10000 + month * 100 + day;
}

function listOverdueDevices(ledger, today) {
    const todayVal = parseDateValue(today);
    const overdueList = [];

    for (const tag in ledger) {
        const device = ledger[tag];
        if (device.status === "CheckedOut" && device.dueDate) {
            const dueVal = parseDateValue(device.dueDate);
            if (dueVal < todayVal) {
                overdueList.push(device)
            }
        }
    }

    return overdueList.sort((a, b) => parseDateValue(a.dueDate) - parseDateValue(b.dueDate));
}

function serializeLedger(ledger) {
    return JSON.stringify(ledger);
}

function loadLedger(json) {
    return JSON.parse(json);
}
