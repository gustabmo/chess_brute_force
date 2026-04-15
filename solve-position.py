## chess-brute-force solve-position.py 
## 2026-04-15 guexel@gmail.com: starting to write


uses chess


class OneMove:
	def __init__ ( self, move_or_fen_if_root_or_moves_if_initial_moves, prev, is_fixed_moves=False ):
		self.prev = prev
		self.is_fixed_moves = is_fixed_moves # the move is part of the fixed initial moves given as input

		if not self.is_fixed_moves:
			if self.prev:
				self.move = move_or_fen_if_root_or_moves_if_initial_moves
			else:
				self.fen = move_or_fen_if_root_or_moves_if_initial_moves
		else:
			if self.prev:
				self.move = gettoken do move_or_fen_if_root_or_moves_if_initial_moves
				self.next_fixed_moves = o que restou do move_or_fen_if_root_or_moves_if_initial_moves
			else:
				self.fen = '' # starting position
				self.next_fixed_moves = move_or_fen_if_root_or_moves_if_initial_moves

		if self.prev:
			self.prev.nexts.push ( self )

		self.nexts = []
		self.state = stUndefined

		self.SetStateAndCreateNextMoves()
		self.Solve()

	def BoardAfterThisMove():
		if (self.prev):
			return self.prev.BoardAfterThisMove.move ( self.move )
		else:
			return create Board from string ( self.fen )

	def SetStateAndCreateNextMoves():
		let board = self.BoardAfterThisMove()
		if board.is_checkmate():
			self.State = stWin
		elif board.can_claim_draw():
			self.State = stDraw
		else:
			self.State = stUndefined
			for m in board.valid_movements():
				create OneMove ( m, self )

	def Solve():
		if self.state == stUndefined:
			all_nexts_are_wins = True
			one_next_is_loss = False

			for n in nexts:
				n.Solve()
				if (n.state != stWin):
					all_nexts_are_wins = False
				if (n.state == stLoss):
					one_next_is_loss = True

			if (all_nexts_are_wins):
				self.state = stLoss
			elif (one_next_is_loss):
				self.state = stWin
			else:
				self.state = stDraw



















