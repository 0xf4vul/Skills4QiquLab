# Skill Templates

## Minimal Skill

```md
# [Skill Name]

## Purpose
[What recurring problem does this solve?]

## Use when
[Trigger conditions]

## Do not use when
[Boundary conditions]

## Inputs
[Required and optional inputs]

## Workflow
1. [Step]
2. [Step]
3. [Step]

## Output
[Exact output contract]

## Failure modes
- [Failure]
- [Failure]

## Evaluation
- [Criterion]
- [Criterion]
```

## Production Skill

```md
# [Skill Name]

## Purpose
...

## Scope
### In scope
...
### Out of scope
...

## Inputs
...

## Procedure
1. Understand intent
2. Identify hard constraints
3. Transform or reason
4. Validate semantic preservation
5. Produce the requested output

## Output contract
...

## Model adaptation
### Model A
...
### Model B
...

## Failure modes
...

## Examples
### Input
...
### Output
...
### Why
...

## Evaluation rubric
- Intent preservation
- Constraint preservation
- Output usefulness
- Robustness
- Model compatibility
```

## Evaluation case

```md
### Case
[short description]

**Input:** ...
**Expected:** ...
**Actual:** ...

**Checks:** intent / constraints / consistency / model execution

**Result:** pass / revise
```
