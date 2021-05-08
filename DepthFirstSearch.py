class ShortestPathDFSSolver(object):

    def __init__(self, display_width, display_height, block_size):
        # Game parameters
        self.display_width = display_width
        self.display_height = display_height
        self.block_size = block_size

        # Action space
        self.actions = {
            0:'left',
            1:'right',
            2:'up',
            3:'down'
        }

    def move(self, snake_list, fruit_node):
        #will be called by main function and used to feed information to this algorithm
        self.snake_list = snake_list
        self.fruit_node = fruit_node
        self.starting_node = snake_list[-1]
        
        shortest_path = self.shortest_path(self.starting_node, self.fruit_node, self.snake_list[1::])
        #check if shortest path exist.
        if shortest_path:
            return shortest_path
        return None

    def possible_action(self, starting_node, snake_list,direction):
        #check for available actions
        #get previous direction
        if len(direction)!=0:
            direction = direction[0]
        
        #initiate pos_actions array
        pos_actions = [[0],[0],[0],[0]]


        #check in all four directions
        if (starting_node[0]+self.block_size < self.display_width and [starting_node[0]+self.block_size, starting_node[1]] not in snake_list) and direction!='left':
            pos_actions[3] = [[starting_node[0]+self.block_size, starting_node[1]],['right']]
        else:
            pos_actions[3] = [0]
        if(starting_node[0]-self.block_size > 0 and [starting_node[0]-self.block_size, starting_node[1]] not in snake_list) and direction!='right': 
            pos_actions[2] = [[starting_node[0]-self.block_size, starting_node[1]],['left']]
        else:
            pos_actions[2] = [0]
        if (starting_node[1]+self.block_size < self.display_height and [starting_node[0], starting_node[1]+self.block_size] not in snake_list) and direction!='up':
            pos_actions[1] = [[starting_node[0], starting_node[1]+self.block_size],['down']]
        else:
            pos_actions[1] = [0]
        if (starting_node[1]-self.block_size > 0 and [starting_node[0], starting_node[1]-self.block_size] not in snake_list) and direction!='down':
            pos_actions[0] = [[starting_node[0], starting_node[1]-self.block_size],['up']]
        else:
            pos_actions[0] = [0]
        
        #return available actions
        return pos_actions


    def shortest_path(self, start, end, snake_list):
        stack = [[start,[]]]
        #Add snake list in visited node array to avoid snake bumping into itself.
        visited_nodes = [list(x) for x in snake_list]
        while stack:
            #stack is last in first out
            current_node = stack.pop()
            path = current_node[1]
            if len(path) == 0:
                curr_direction = ''
            else:
                curr_direction = path[-1]
            if (current_node[0] == end):
                #when current node is end return path
                return path
            if current_node[0] not in visited_nodes:
                visited_nodes.append([current_node[0][0],current_node[0][1]])
                #check for nodes (possible actions) if current not in visited node
                for action in self.possible_action(current_node[0], visited_nodes, curr_direction):
                    if action[0] == 0:
                        continue
                    #append path to new path and push it to stack
                    new_path = path + [action[1]]
                    stack.append([action[0],new_path])
                