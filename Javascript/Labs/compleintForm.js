function validateForm() {
    const fullName = document.getElementById('full-name')?.value || '';
    const email = document.getElementById('email')?.value || '';

    const orderNo = document.getElementById('order-no')?.value || '';
    const productCode = document.getElementById('product-code')?.value || '';
    const quantity = document.getElementById('quantity')?.value || '';

    const otherComplaint = document.getElementById('other-complaint');
    const complaintDescription = document.getElementById('complaint-description')?.value || '';

    const otherSolution = document.getElementById('other-solution');
    const solutionDescription = document.getElementById('solution-description')?.value || '';

    // Verificación de casillas de verificación y botones de opción marcados
    const complaintsChecked = document.
        querySelectorAll('#complaints-group input[type="checkbox"]:checked').length > 0;
    const solutionsChecked = document.
        querySelectorAll('#solutions-group input[type="radio"]:checked').length > 0;

    // Reglas de validación
    const isFullNameValid = fullName.trim().length > 0;
    const isEmailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
    const isOrderNoValid = /^2024\d{6}$/.test(orderNo.trim());
    const isProductCodeValid = /^[a-zA-Z]{2}\d{2}-[a-zA-Z]\d{3}-[a-zA-Z]{2}\d$/.
        test(productCode.trim());
    const isQuantityValid = /^[1-9]\d*$/.test(quantity.trim());
    const isComplaintsGroupValid = complaintsChecked;
    const isComplaintDescriptionValid = !(otherComplaint && otherComplaint.checked) ||
        complaintDescription.length >= 20;
    const isSolutionsGroupValid = solutionsChecked;
    const isSolutionDescriptionValid = !(otherSolution && otherSolution.checked) ||
        solutionDescription.length >= 20;

    return {
        'full-name': isFullNameValid,
        'email': isEmailValid,
        'order-no': isOrderNoValid,
        'product-code': isProductCodeValid,
        'quantity': isQuantityValid,
        'complaints-group': isComplaintsGroupValid,
        'complaint-description': isComplaintDescriptionValid,
        'solutions-group': isSolutionsGroupValid,
        'solution-description': isSolutionDescriptionValid
    };
}

// 2. Función global para comprobar si todo el formulario es válido
function isValid(validations) {
    return Object.values(validations).every(value => value === true);
}

// 3. Mapeo de campos y sus claves para asignación de eventos 'change'
const fieldMap = [
    { id: 'full-name', key: 'full-name' },
    { id: 'email', key: 'email' },
    { id: 'order-no', key: 'order-no' },
    { id: 'product-code', key: 'product-code' },
    { id: 'quantity', key: 'quantity' },
    { id: 'complaints-group', key: 'complaints-group' },
    { id: 'complaint-description', key: 'complaint-description' },
    { id: 'solutions-group', key: 'solutions-group' },
    { id: 'solution-description', key: 'solution-description' }
];

// Asignar escuchadores de evento 'change' a cada campo o fieldset
fieldMap.forEach(({ id, key }) => {
    const element = document.getElementById(id);
    if (element) {
        element.addEventListener('change', () => {
            const validations = validateForm();
            element.style.borderColor = validations[key] ? 'green' : 'red';
        });
    }
});

// 4. Manejo del evento 'submit' del formulario
const form = document.getElementById('form');
if (form) {
    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const validations = validateForm();
        const formIsValid = isValid(validations); // Se evalúa si TODO el formulario es válido

        // 1. Resaltar visualmente cada campo (verde o rojo)
        fieldMap.forEach(({ id, key }) => {
            const element = document.getElementById(id);
            if (element) {
                element.style.borderColor = validations[key] ? 'green' : 'red';
            }
        });

        // 2. Uso real de formIsValid:
        if (formIsValid) {
            // Código que se ejecuta solo si todos los campos son correctos
            document.getElementById('message-box').
            textContent = 'Formulario enviado con éxito';
        } else {
            document.getElementById('message-box').
            textContent = 'Por favor, corrige los campos marcados en rojo';
        }
    });
}