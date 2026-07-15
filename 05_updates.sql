-- 05_updates.sql
-- Allow joining in-progress rooms as an observer (team=null, role=null).
-- Observers see the board in read-only mode, cannot reveal tiles or give clues.
-- Joining a finished room is blocked.

CREATE OR REPLACE FUNCTION join_room(p_code text, p_nickname text)
RETURNS TABLE(room_id uuid, player_id uuid)
LANGUAGE plpgsql SECURITY DEFINER
AS $$
DECLARE
  v_room   rooms%ROWTYPE;
  v_pid    uuid;
BEGIN
  SELECT * INTO v_room FROM rooms WHERE code = upper(p_code);
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Room not found — check the code and try again.';
  END IF;

  IF v_room.status = 'finished' THEN
    RAISE EXCEPTION 'This game has already finished.';
  END IF;

  -- Two-player lobby cap: only 2 active participants, but observers are fine
  -- once the game is in progress.
  IF v_room.mode = 'two_player' AND v_room.status = 'lobby' THEN
    IF (SELECT COUNT(*) FROM players WHERE players.room_id = v_room.id) >= 2 THEN
      RAISE EXCEPTION 'This two-player room is full.';
    END IF;
  END IF;

  -- Re-use existing player row if this auth user already joined this room.
  SELECT id INTO v_pid
  FROM players
  WHERE players.room_id = v_room.id AND user_id = auth.uid();

  IF v_pid IS NULL THEN
    INSERT INTO players (room_id, user_id, nickname)
    VALUES (v_room.id, auth.uid(), p_nickname)
    RETURNING id INTO v_pid;
  END IF;

  RETURN QUERY SELECT v_room.id, v_pid;
END;
$$;

GRANT EXECUTE ON FUNCTION join_room(text, text) TO authenticated;
