### Geometry Management in Tkinter

Tkinter provides three primary geometry managers to control the placement and layout of widgets within a window. These are:

1. **Pack**: Simplest manager, packs widgets in blocks before placing them in the parent widget.
2. **Grid**: Organizes widgets in a table-like structure.
3. **Place**: Places widgets at absolute positions.

---

## Tkinter `pack` Geometry Manager

The `pack` geometry manager arranges widgets in blocks before placing them in the parent widget. It is ideal for simple layouts where widgets need to be stacked vertically or horizontally.

### Syntax

```python
widget.pack(options)
```

### Common Options

- **`side`**: Specifies which side of the parent widget to pack against. Options: `TOP`, `BOTTOM`, `LEFT`, `RIGHT`.
  ```python
  widget.pack(side=tk.LEFT)
  ```

- **`fill`**: Determines how the widget should expand to fill the available space. Options: `NONE`, `X`, `Y`, `BOTH`.
  ```python
  widget.pack(fill=tk.BOTH)
  ```

- **`expand`**: Boolean option that specifies whether the widget should expand to fill any extra space in the geometry master.
  ```python
  widget.pack(expand=True)
  ```

- **`padx` and `pady`**: Adds extra space around the widget. Values are specified in pixels.
  ```python
  widget.pack(padx=10, pady=10)
  ```

### Example Usage

```python
import tkinter as tk

root = tk.Tk()

# Create three buttons
btn1 = tk.Button(root, text="Button 1")
btn2 = tk.Button(root, text="Button 2")
btn3 = tk.Button(root, text="Button 3")

# Pack buttons with different options
btn1.pack(side=tk.LEFT, padx=5, pady=5)
btn2.pack(side=tk.LEFT, padx=5, pady=5)
btn3.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
```

In this example, three buttons are packed side-by-side with padding between them.

### Tips for Using `pack`

- Use `side` to specify which edge of the parent to pack against.
- Use `fill` to make widgets expand and fill available space.
- Combine `expand` with `fill` to fully utilize the available space in the parent widget.
- `padx` and `pady` can help create visually appealing layouts by adding space around widgets.

The `pack` geometry manager is straightforward and efficient for many layouts, but for more complex arrangements, consider using the `grid` or `place` geometry managers.
