import agents as ag

def HW2Agent() -> object:
    oldPercepts = [('None', 'Clean')]
    oldActions = ['NoOp']
    count = 0
    def program(percept):
        bump, status = percept
        lastBump, lastStatus = program.oldPercepts[-1]

        if status == 'Dirty':

            action = 'Suck'

        else:





                #last = 'r'
         #action = 'Up'

            #if bump == 'None':
             #   action = 'Up'
            #else:
             #   action = 'Right'



#            if lastStatus == 'Right'

            #if bump == 'None':

               # action = 'up'
               #lastBump = 'Left'

            #else:
             #   action = 'Right'
              #  lastBump = 'Right'
                        #start here

            #if lastBump == 'Right':
             #   action = 'Left'
              #  lastBump = 'Left'
            #else:
               # action = 'Right'
                #lastBump ='Right'




            if bump == 'None':
                action = 'Right'
            else:
                action = 'Left'

        program.oldPercepts.append(percept)
        program.oldActions.append(action)
        return action

    # assign static variables here
    program.oldPercepts = [('None', 'Clean')]
    program.oldActions = ['NoOp']

    agt = ag.Agent(program)
    # assign class attributes here:
    # agt.direction = ag.Direction('left')

    return agt
