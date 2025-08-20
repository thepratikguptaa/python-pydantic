# Python-Pydantic

A repository for learning and exploring the features of the Pydantic library in Python. This project contains several examples, each focusing on a different aspect of Pydantic.

## Project Structure and Examples

The project is divided into several directories, each containing a specific example:

### `01-foundation`

This directory contains the basics of creating a Pydantic model. The `first_model.py` file shows how to define a simple `User` model and how Pydantic performs data conversion and validation.

### `02-fields-validation`

The `fields.py` file demonstrates how to use `Field` for more advanced field validation, including setting a min/max length for a string.

### `03-model-behavior`

This section explores how to customize model behavior. The `validator.py` file shows how to use:
- `@field_validator` to validate a specific field.
- `@model_validator` to perform validation on the entire model.
- `@computed_field` to add a computed property to a model.

### `04-nested-models`

The `nested_model.py` file explains how to create and use nested Pydantic models, which is useful for representing complex data structures.

### `05-serialization`

This example covers serialization of Pydantic models. The `serialization.py` file demonstrates how to use:
- `model_dump()` to convert a model instance to a dictionary.
- `model_dump_json()` to convert a model instance to a JSON string.

### `fastapi`

This directory contains an example of how to use Pydantic models with the FastAPI framework. The `fastapi_example.py` file shows how Pydantic is used for:
- Request body validation in a POST endpoint.
- Dependency injection with a `Settings` model.


## Pydantic Features Used

Here is a summary of the Pydantic features demonstrated in this project:

*   **BaseModel:** The fundamental building block in Pydantic. You inherit from it to create your data models with typed fields.
*   **Data Coercion:** Pydantic automatically tries to convert incoming data to the declared field types, like converting the string `"101"` to the integer `101`.
*   **Field:** This function lets you add extra configuration and validation to your model's fields, such as setting minimum/maximum length or descriptions.
*   **@field_validator:** A decorator that allows you to define custom validation logic for a single field, which is useful for complex checks.
*   **@model_validator:** A decorator for creating validation rules that depend on multiple field values at once, allowing you to enforce complex logic across the entire model.
*   **@computed_field:** This decorator lets you add new fields to your model whose values are calculated from other fields, including the result in the model's output.
*   **Nested Models:** Pydantic allows you to compose models by using one model as a type for a field in another, which helps in representing complex, structured data.
*   **Recursive Models:** These are models that can contain other instances of themselves, which is perfect for hierarchical data like comment threads.
*   **Serialization with `model_dump()`:** This method converts your Pydantic model instance into a Python dictionary, which is useful for working with the data in a standard Python format.
*   **JSON Serialization with `model_dump_json()`:** This method serializes the model instance directly into a JSON formatted string, which is more efficient than creating a dictionary first.
*   **FastAPI Integration:** Pydantic models are a core part of FastAPI and are used to define the shape of incoming request data for automatic validation and documentation.
*   **EmailStr:** A special data type provided by Pydantic for validating email addresses, ensuring the provided string is in a valid email format.