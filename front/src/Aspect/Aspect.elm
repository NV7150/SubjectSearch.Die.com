module Aspect.Aspect exposing (..)
import Aspect.Model exposing (..)


update : Msg -> AspectModel ->  ( AspectModel, Cmd Msg )
update msg model =
    case msg of
        _ ->
             ( model, Cmd.none )
