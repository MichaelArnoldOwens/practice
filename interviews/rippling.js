import React, { useCallback, useEffect, useState } from "react";
import Debugger from "./Debugger";

import "./App.css";

// -- WELCOME! --
// Rippling is working on a generic “Form” component as part of
// a larger component library that will allow our developers
// to quickly stand up forms without having to worry about
// scaffolding individual inputs, submit buttons, etc.
// in our application. Let’s build a quick prototype of that today.
// -- END PROMPT! --

// Part 1: Form Schema Definition
// What should the "schema" for a component like this look like?
// Let's explore different use cases like:
// - Additional field types
// - Validations
// - Other customizations
/*
formats to support:
  text, number, email
  [{
    format: 'text' | 'number' | 'email' 
    placeholder?: string
    initialValue?: string
    label: string
    validation?: () => boolean
  }]
*/

// we can take some hypothetical use-case as an exmaple to build
// First name
// Last name
// Age
const INPUT_FORMAT = {
  TEXT: 'text',
  NUMBER: 'number',
  EMAIL: 'email'
}

const formSchema = [
  {
    format: INPUT_FORMAT.TEXT,
    label: 'First name',
    placeholder: 'First name',
    validation: (val) => val.length > 0
  },
  {
    format: INPUT_FORMAT.TEXT,
    label: 'Last Name',
    placeholder: 'Last Name'
  },
  {
    format: INPUT_FORMAT.NUMBER,
    label: 'Age',
    placeholder: 'Age'
  }
];

// Part 2: Let's build our form component
// Let's try to hit a few of the use cases from above
// uuid()
const Input = ({format, label, value, placeholder, updateState, position, validation}) => {
  // console.log('updateState:', updateState)
  // console.log(validation)
  return <div>
    <div>{label}</div>
    <input type={format} value={value} onChange={e => updateState({value: e.target.value, position, label, isValid: validation ? validation(e.target.value) : true})} />
    </div>
}

const Form = ({ formSchema, onSubmit }) => {
  const [formDataObj, setFormDataObj] = useState([])
  const [areValid, setAreValid] = useState([false])
  const [isValidForm, setIsValidForm] = useState(false)
  // console.log(formDataObj)

  useEffect(() => {
    console.log('areValid:', areValid)
    setIsValidForm(areValid.every(x => !!x))
  },[areValid, setIsValidForm])

  const updateState = ({label, value, position, isValid}) => {
    // console.log('value:', value)
    // console.log(formDataObj)
    // console.log('areValid', areValid)
    console.log('isValid in updateSTate', isValid)
    // areValid[position] = isValid
    setAreValid(curr => {
      curr[position] = isValid
      return curr
    })
    // formDataObj[position] = {label, value}
    setFormDataObj(curr => {
      curr[position] = {label, value}
      return curr
    })
  }



  console.log('isValidForm:', isValidForm)

  return <div>
    {formSchema.map((v, idx) => <Input {...v} position={idx} updateState={updateState} value={formDataObj[idx]?.value} />) }
    <button disabled={!isValidForm} onClick={() => onSubmit(formDataObj)}>submit</button>
  </div>;
};

const App = () => {
  const [submittedValues, setSubmittedValues] = useState();
  const onSubmit = useCallback((formData) => {
    console.log('on submit', formData)
    // {"name": "John", } return the bare minimum obj back
    setSubmittedValues(formData);
  }, []);

  return (
    <div className="page-container">
      <div className="main-container">
        <div className="form-container">
          <Form formSchema={formSchema} onSubmit={onSubmit} />
        </div>
        <Debugger values={submittedValues} />
      </div>
    </div>
  );
};

export default App;

