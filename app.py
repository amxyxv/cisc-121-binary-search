import gradio as gr
import random

def binary_search(arr, target):
    steps = []
    left = 0
    right = len(arr) - 1
    step_count = 1

    steps.append(f"Initial sorted array: {arr}")
    steps.append(f"Searching for target: {target}")

    while left <= right:
        mid = (left + right) // 2
        steps.append(f"Step {step_count}: Checking middle index {mid} (value = {arr[mid]})")

        if arr[mid] == target:
            steps.append(f"✅ Target {target} FOUND at index {mid}!")
            return mid, "\n".join(steps)
        elif arr[mid] < target:
            steps.append(f"   {target} is larger → Search right half (indices {mid+1} to {right})")
            left = mid + 1
        else:
            steps.append(f"   {target} is smaller → Search left half (indices {left} to {mid-1})")
            right = mid - 1
        step_count += 1

    steps.append(f"❌ Target {target} not found in the array.")
    return -1, "\n".join(steps)

def run_search(target_str, arr_str=None):
    if not target_str.strip():
        return "Please enter a target number.", "Error: Target cannot be empty."

    try:
        target = int(target_str)
    except ValueError:
        return "Error: Please enter a valid integer.", ""

    # Use provided array or generate new one
    if arr_str and arr_str.strip():
        try:
            arr = sorted([int(x) for x in arr_str.strip("[]").split(",")])
        except:
            arr = sorted(random.sample(range(0, 101), 15))
    else:
        arr = sorted(random.sample(range(0, 101), 15))

    index, log = binary_search(arr, target)

    if index != -1:
        result = f"✅ Found at index {index} in array {arr}"
    else:
        result = f"❌ Not found in array {arr}"

    return result, log

# Gradio Interface
with gr.Blocks(title="Binary Search Simulator - CISC-121") as demo:
    gr.Markdown("# 🔍 Binary Search Algorithm Simulator")
    gr.Markdown("### Educational Demo for CISC-121\nEnter a target and watch how Binary Search efficiently narrows down the search space step by step.")

    with gr.Row():
        with gr.Column():
            target_input = gr.Textbox(label="Target Number", placeholder="e.g. 45")
            array_input = gr.Textbox(label="Custom Sorted Array (optional)", placeholder="[10, 23, 45, 67, 89]", lines=1)
            btn = gr.Button("Run Binary Search", variant="primary")
            new_array_btn = gr.Button("Generate New Random Array")

        with gr.Column():
            result_box = gr.Textbox(label="Final Result", interactive=False)
            steps_box = gr.Textbox(label="Step-by-Step Explanation", lines=20, interactive=False)

    # Generate new array functionality
    def generate_array():
        arr = sorted(random.sample(range(0, 101), 15))
        return str(arr)

    new_array_btn.click(generate_array, outputs=array_input)

    btn.click(run_search, inputs=[target_input, array_input], outputs=[result_box, steps_box])

    gr.Markdown("""
    **How it works:**  
    - The array is always sorted.  
    - Binary Search repeatedly divides the search interval in half (O(log n) time).  
    - Try different targets and watch the steps!
    """)

if __name__ == "__main__":
    demo.launch()