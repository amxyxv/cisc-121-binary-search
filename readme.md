# Binary Search Algorithm Simulator - CISC-121

## Demo
*(Screenshots / GIF will be added here after running locally)*

**Live Hugging Face App:**  
[Add your HF link here after deployment]

## Problem Breakdown & Computational Thinking

**Why Binary Search?**  
I chose Binary Search because it is a fundamental efficient searching algorithm that demonstrates the power of **divide-and-conquer**. It only works on sorted arrays and is dramatically faster than Linear Search (logarithmic vs linear time). This makes it perfect for teaching algorithm efficiency.

**Computational Thinking:**
- **Decomposition**: The problem breaks into initializing pointers (`left`, `right`), calculating the middle index, comparing values, and narrowing the search range.
- **Pattern Recognition**: The algorithm repeatedly halves the search space based on whether the target is smaller or larger than the middle element.
- **Abstraction**: Complex index calculations are hidden; the user sees clear, human-readable step explanations with arrows and emojis.
- **Algorithm Design**: Input (target + optional array) → Generate/validate sorted array → Binary search loop with logging → Output (result + detailed step log).

## Steps to Run Locally
1. Clone/download the repository.
2. Open a terminal in the project folder.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `python app.py`
5. Open the local URL shown in the terminal.

## Hugging Face Link
(Will be added after deployment)

## Testing & Verification
I tested the following cases:
- Target present in the middle, beginning, and end of the array.
- Target not present in the array.
- Target smaller or larger than all elements.
- Invalid inputs (letters, empty field) — handled with clear error messages.
- Custom array input vs random array.

All cases produced correct results and informative step logs.

## Author
Ameya  
CISC-121 Project  
Thank you to the course guidelines and Gradio documentation.
