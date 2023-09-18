import pygame as py
from pygame.locals import *
import time

class Gui:
   def __init__(self, size, width, height, crest, zero, bot):
      py.init()
      self.bot = bot
      self.font = py.font.SysFont("Aerial", 30)
      self.field = [['*' for j in range(size)] for i in range(size)]
      self.padding = 10
      self.size = size
      self.width = width
      self.height = height
      self.x_pad = (width-2*self.padding) // size
      self.y_pad = (height-2*self.padding) // size
      self.size_img = self.x_pad-2

      self.crest_img = py.image.load(crest)
      self.zero_img = py.image.load(zero)
      self.zero_img = py.transform.scale(self.zero_img, (self.size_img, self.size_img))
      self.crest_img = py.transform.scale(self.crest_img, (self.size_img, self.size_img))

      self.screen = py.display.set_mode((width, height))
      self.screen.fill((255, 255, 255))
      self.bot_symbol = self.bot.bot_symbol
      self.player_symbol = self.bot.player_symbol
      py.display.set_caption("Tic tac toe")

   def draw_lines(self):
      for i in range(self.size + 1):
         py.draw.line(self.screen, (0, 0, 0), (self.padding, self.padding + i * self.y_pad), (self.width - self.padding, self.padding + i * self.y_pad))
      for i in range(self.size + 1):
         py.draw.line(self.screen, (0, 0, 0), (self.padding + i * self.x_pad, self.padding), (self.padding + i * self.x_pad, self.height - self.padding))

   def add(self, pos, symbol):
      i = (pos[0] - self.padding) // self.x_pad
      j = (pos[1] - self.padding) // self.y_pad
      if self.field[i][j] == '*':
         self.field[i][j] = symbol
         return (i, j)
      return (-1, -1)

   def draw_symbols(self):
      for i in range(self.size):
         for j in range(self.size):
            if self.field[i][j] == 'X':
               self.screen.blit(self.crest_img, (self.padding + 1 + i * self.x_pad, self.padding + 1 + j * self.y_pad))
            elif self.field[i][j] == 'O':
               self.screen.blit(self.zero_img, (self.padding + 1 + i * self.x_pad, self.padding + 1 + j * self.y_pad))

   def draw_control_panel(self):
      while True:
         for event in py.event.get():
               if event.type == QUIT:
                  py.quit()
                  return
               elif event.type == MOUSEBUTTONDOWN:
                  x, y = py.mouse.get_pos()
                  if 200 <= x <= 300 and 100 <= y <= 150:
                     break
         py.draw.rect(self.screen, (0, 0, 0), [200, 100, 300, 150])
         text = self.font.render("Play", 1, py.Color("White"))
         self.screen.blit(text, (230, 125))
         py.display.update()
      self.draw()

   def get_coords(self, pair):
      return (self.padding + pair[0] * self.x_pad, self.padding + pair[1] * self.y_pad)

   def set_winner(self):
      winner = self.bot.tic_tac_toe.end_of_game(self.field)
      if winner == self.bot_symbol:
         py.display.set_caption("Bot wins!")
         return self.bot_symbol
      elif winner == self.player_symbol:
         py.display.set_caption("Human wins!")
         return self.player_symbol
      elif winner == 'Draw':
         py.display.set_caption("No one wins!")
         return 'D'
      else:
         return None

   def check_end(self):
      symbol = self.set_winner()
      if symbol != None:
         self.draw_lines()
         self.draw_symbols()
         py.display.flip()
         time.sleep(5)
      return symbol

   def draw(self):
      flag = True
      player_turns, bot_turns = [], []
      end = None
      while end == None:
         self.draw_lines()
         self.draw_symbols()
         py.display.flip()

         if flag == True:
            flag = False
            bot_turns.append(self.add(self.get_coords(self.bot.make_bot_move(player_turns, bot_turns)), self.bot_symbol))
            end = self.check_end()
            if end != None:
               break

         for event in py.event.get():
               if event.type == QUIT:
                  py.quit()
                  return
               elif event.type == MOUSEBUTTONDOWN:
                  flag = True
                  player_turns.append(self.add(py.mouse.get_pos(), self.player_symbol))
         end = self.check_end()
         if end != None:
            break
         #if symbol == 'X' or symbol == 'O' or symbol == 'D':
            #break
