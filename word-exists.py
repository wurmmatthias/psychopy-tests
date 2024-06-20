from psychopy import visual, event, core, data, logging, gui

# Set up the experiment
exp_info = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=exp_info, title='Word Existence Quiz')
if dlg.OK == False:
    core.quit()  # User pressed cancel

# Create a filename for logging data
filename = f"data/{exp_info['participant']}_data"
this_exp = data.ExperimentHandler(dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # This outputs to the screen, not a file

# Define words and their existence status
words = {
    'apple': True,
    'sdfghj': False,
    'banana': True,
    'qwerty': False
}

# Create a window
win = visual.Window([800, 600], fullscr=False, color="white")

# Create a text stimulus
text_stim = visual.TextStim(win, text='', height=0.1, color="black")

# Instructions
instructions = visual.TextStim(win, text="Press 'y' if the word exists and 'n' if it does not.\nPress any key to start.", height=0.08, color="black")
instructions.draw()
win.flip()
event.waitKeys()

# Run the trial
for word, exists in words.items():
    text_stim.text = word
    text_stim.draw()
    win.flip()

    keys = event.waitKeys(keyList=['y', 'n', 'escape'])
    if 'escape' in keys:
        core.quit()
    
    response = keys[0] == 'y'
    correct = response == exists

    # Log data
    this_exp.addData('word', word)
    this_exp.addData('response', response)
    this_exp.addData('correct', correct)
    this_exp.nextEntry()

    # Provide feedback
    #feedback = "Correct!" if correct else "Wrong!"
    #feedback_stim = visual.TextStim(win, text=feedback, height=0.1, color="black")
    #feedback_stim.draw()
    #win.flip()
    #core.wait(1)

# Clean up
this_exp.saveAsWideText(filename + '.csv')
this_exp.saveAsPickle(filename)
win.close()
core.quit()
