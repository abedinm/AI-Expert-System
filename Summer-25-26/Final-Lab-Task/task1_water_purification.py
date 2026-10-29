# Final Lab Task 1 - Water Purification Agent


def show_state(label, turbidity, tds, bacteria, ph):
    print(label + ": Turbidity = " + str(turbidity) + ", TDS = " + str(tds) +
          ", Bacteria = " + str(bacteria) + ", pH = " + str(ph))


def goal_reached(turbidity, tds, bacteria, ph):
    return turbidity <= 1 and tds <= 300 and not bacteria and 6.5 <= ph <= 8.5


# sensor readings
turbidity = 5.0
tds = 700
bacteria = True
ph = 5.8

show_state("Initial water quality", turbidity, tds, bacteria, ph)

sedimentation_done = False

# condition-action rules
while not goal_reached(turbidity, tds, bacteria, ph):
    if turbidity > 1 and not sedimentation_done:
        print("→ Turbidity > 1 → Action Taken: Sedimentation")
        turbidity = round(turbidity * 0.1, 1)
        sedimentation_done = True
    elif turbidity > 1:
        print("→ Turbidity still > 1 → Action Taken: Filtration")
        turbidity = round(turbidity * 0.5, 1)
    elif tds > 300:
        print("→ TDS > 300 → Action Taken: Reverse Osmosis")
        tds = int(tds * 0.4)
    elif bacteria:
        print("→ Bacteria = True → Action Taken: UV Treatment")
        bacteria = False
    elif ph < 6.5:
        print("→ pH < 6.5 → Action Taken: Add Chemicals")
        ph = 7.2
    else:
        print("→ pH > 8.5 → Action Taken: Add Chemicals")
        ph = 7.2

    # print the state after each action
    show_state("   Updated state", turbidity, tds, bacteria, ph)

show_state("Water quality after treatment", turbidity, tds, bacteria, ph)
print("Goal Achieved: Water is purified and safe for drinking.")
