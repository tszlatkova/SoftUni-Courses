from .player import Player


class Guild:

    def __init__(self, name: str) -> None:
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        p: Player = next((p for p in self.players if p.name == player_name), None)
        if p:
            p.guild = "Unaffiliated"
            self.players.remove(p)
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = '\n'.join([p.player_info() for p in self.players])
        return f"Guild: {self.name}\n{players_info}"
