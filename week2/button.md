# Tkinter Button

The Button widget in Tkinter is used to create clickable buttons in a Python application. These buttons can display text or images and trigger functions when clicked.

## Syntax

```python
b = Button(master, option=value, ....)
```

### Parameters

- **master**: The parent window.
- **options**: Key-value pairs to customize the button.
  1. **activebackground**: Background color when the button is hovered.
  2. **activeforeground**: Text color when the button is hovered.
  3. **bd**: Border width in pixels (default is 2).
  4. **bg**: Background color.
  5. **command**: Function to call when the button is clicked.
  6. **fg**: Text color.
  7. **font**: Font for the button's text.
  8. **height**: Height in text lines or pixels.
  9. **highlightbackground**: Background color when focused.
  10. **image**: Image to display instead of text.
  11. **justify**: Text alignment (LEFT, CENTER, RIGHT).
  12. **padx**: Horizontal padding.
  13. **pady**: Vertical padding.
  14. **relief**: Border type (FLAT, SUNKEN, RAISED, GROOVE, RIDGE).
  15. **state**: Button state (NORMAL, ACTIVE, DISABLED).
  16. **underline**: Index of the character to underline.
  17. **width**: Width in letters or pixels.
  18. **wraplength**: Wrap text to fit within this length.

## Methods

### flash()

Makes the button flash between active and normal colors.

### invoke()

Simulates a button click by calling the button's command function.

