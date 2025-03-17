# Calendar Parser: Natural Language to iCalendar Format

This project implements a natural language understanding system that converts free-form calendar expressions into structured iCalendar format using language models. It compares the performance of standard and quantized models for efficient calendar parsing.

## Project Overview

Calendar Parser interprets diverse natural language scheduling expressions and converts them into standardized iCalendar format variables. The system handles a wide range of temporal expressions including:

- Simple relative dates: "in 2 days", "tomorrow 10am"
- Recurring events: "every wed 2pm", "weekly on friday from 18 jun til 20 oct"
- Complex time expressions: "every 10 minutes between 2 and 7pm"
- Timezone specifications: "8pm EST", "9:19am madrid time"
- Reminders: "remind 30m before 10am"
- Special calendaring features: "first mon of next quarter", "weekdays minus thursday"

## Repository Structure

- `model_comparison.ipynb`: Main notebook comparing standard and quantized models
- `standard_model_results.csv`: Performance results from the standard model
- `quantized_model_results.csv`: Performance results from the quantized model
- `taxonomy.md`: Comprehensive categorization of supported scheduling expressions
- `labelled_taxonomy_examples.md`: Examples of scheduling expressions with expected outputs
- `relativedelta.ipynb`: Notebook for datetime calculations with relativedelta
- `LM.ipynb`: Basic language model interaction examples
- `example.ics`: Sample iCalendar format output

## Installation

```bash
# Install all requirements at once
pip install -r requirements.txt

# Alternatively, you can install individual packages
# pip install accelerate
# pip install gguf
# pip install transformers
# pip install pandas numpy matplotlib
# pip install python-dateutil
```

## Usage

The project provides a function to generate calendar outputs from natural language:

```python
response, gen_time = generate_calendar_output(model, tokenizer, "next monday 3pm")
print(response)
# Output:
# DTSTART: 20250317T150000
# DTEND: 20250317T160000
```

## Model Details

The project compares two models:
- **Standard Model**: Qwen2.5-0.5B-Instruct full precision model
- **Quantized Model**: Qwen2.5-0.5B-Instruct quantized model for improved efficiency

## Methodology

1. A comprehensive taxonomy of calendar expressions was created
2. Test datasets were constructed across different expression categories
3. Both models were evaluated on:
    - Generation time
    - Output validity (correct iCalendar format)
    - Presence of required fields (DTSTART, DTEND/DURATION, RRULE for recurring events)
    - Time calculation accuracy

## Results

The comparison shows:
- Quantized models offer significant speed improvements (~30-40% faster)
- Minor differences in output format between standard and quantized models
- Both models handle simple cases well, but complex expressions with recurrence rules or timezone specifications show more variability

## Contributors

Machine Learning Practical group project at the University of Edinburgh.

## License

[Specify license information]