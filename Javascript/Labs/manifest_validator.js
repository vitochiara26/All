function normalizeUnits(manifest) {
    const copiedManifest = { ...manifest };
    if (copiedManifest.unit === "lb") {
        copiedManifest.weight *= 0.45
    }
    copiedManifest.unit = "kg"

    return copiedManifest;
}

function validateManifest(manifest) {
    const errors = {};
    //containerId
    if (!manifest.hasOwnProperty("containerId")) {
        errors.containerId = "Missing";
    } else if (!Number.isInteger(manifest.containerId) || manifest.containerId <= 0) {
        errors.containerId = "Invalid";
    }
    //destination
    if (!manifest.hasOwnProperty("destination")) {
        errors.destination = "Missing"
    } else if (typeof manifest.destination !== "string" ||
        manifest.destination.trim().length === 0) {
        errors.destination = "Invalid"
    }
    //weight
    if (!manifest.hasOwnProperty("weight")) {
        errors.weight = "Missing"
    } else if (typeof manifest.weight !== "number" ||
        isNaN(manifest.weight) || manifest.weight <= 0) {
        errors.weight = "Invalid"
    }
    //unit
    if (!manifest.hasOwnProperty("unit")) {
        errors.unit = "Missing"
    } else if (manifest.unit !== "kg" && manifest.unit !== "lb") {
        errors.unit = "Invalid"
    }
    //hazmat
    if (!manifest.hasOwnProperty("hazmat")) {
        errors.hazmat = "Missing"
    } else if (typeof manifest.hazmat !== "boolean") {
        errors.hazmat = "Invalid"
    }

    return errors;
}

function processManifest(manifest) {
    const validation = validateManifest(manifest)

    if (Object.keys(validation).length === 0) {
        const validAndNormalManifest = normalizeUnits(manifest)
        console.log(`Validation success: ${validAndNormalManifest.containerId}`)
        console.log(`Total weight: ${validAndNormalManifest.weight} kg`)
    } else {
        console.log(`Validation error: ${manifest.containerId}`)
        const invalidManifest = validateManifest(manifest)
        console.log(invalidManifest)
    }
    return ''
}

const boatManifest = {
    containerId: 68,
    destination: "Salinas",
    weight: 101,
    unit: "lb",
    hazmat: true
}

const planeManifest = {
    containerId: 1,
    destination: "Santa Cruz",
    weight: 304,
    unit: "kg",
    hazmat: false
}

const carManifest = {
    containerId: 55,
    destination: "Carmel",
    weight: 400,
    unit: "lb",
    hazmat: false
}

const testManifest = {
    containerId: -88,
    destination: "Soledad",
    weight: NaN
}

console.log(normalizeUnits(boatManifest))
console.log(validateManifest(planeManifest))
console.log(processManifest(carManifest))
console.log(processManifest(testManifest))
